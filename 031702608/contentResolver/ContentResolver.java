package com.content;

import com.google.gson.Gson;

import java.io.*;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ContentResolver {
    public static void main(String[] args) {
        String s = readToString().trim();
        String[] split = s.split("\r\n\r\n");
        ArrayList<UserInfo> list = new ArrayList<>();
        for (String info : split) {
            UserInfo userInfo = new UserInfo();
            //解析出姓名
            String[] arr1 = info.split(",");
            String name = arr1[0];
            String phone = checkCellphone(arr1[1]);
            userInfo.set姓名(name);
            userInfo.set手机(phone);
            String addr = arr1[1].split(phone)[0] + arr1[1].split(phone)[1].replace(".", "");
      
            ArrayList<String> addrs = new ArrayList<>();
            Map<String, String> stringStringMap = MyAddrUtils.addressFormat(addr);
            if (stringStringMap.get("province") != null) {
            	addrs.add(stringStringMap.get("province"));
            }
            if (stringStringMap.get("city") != null) {
            	addrs.add(stringStringMap.get("city"));
            }
            if (stringStringMap.get("county") != null) {
            	addrs.add(stringStringMap.get("county"));
            }
            if (stringStringMap.get("town") != null) {
            	addrs.add(stringStringMap.get("town"));
            }
            if (stringStringMap.get("village") != null) {
            	addrs.add(stringStringMap.get("village"));
            }   
        	userInfo.set地址(addrs);
            list.add(userInfo);
        }
        Gson gson = new Gson();
        String jsonStr = gson.toJson(list);
        System.out.println(jsonStr);
        writeToFile(jsonStr);

    }


    private static void writeToFile(String content) {
        try {
            //定义文件路径，没有该文件会自动创建，如果路径有文件夹，一定要有，不会自动创建文件夹
            String filename = "src/outJson.txt";
            File file = new File(filename);
            if (!file.exists()) {
                file.createNewFile();
            }
            byte[] b = content.getBytes();  //将字符串转换成字节数
            OutputStream out = null;
            try {
                out = new FileOutputStream(file);   //实例化OutpurStream
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }

            //写入
            out.write(b);       //写入
            out.close();        //关闭
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static String readToString() {
        String encoding = "UTF-8";
        File file = new File("src/content");
        Long filelength = file.length();
        byte[] filecontent = new byte[filelength.intValue()];
        try {
            FileInputStream in = new FileInputStream(file);
            in.read(filecontent);
            in.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            return new String(filecontent, encoding);
        } catch (UnsupportedEncodingException e) {
            System.err.println("The OS does not support " + encoding);
            e.printStackTrace();
            return null;
        }
    }

    /**
     * 查询符合的手机号码
     *
     * @param str
     */
    public static String checkCellphone(String str) {
        String phone = "";
        // 将给定的正则表达式编译到模式中
        Pattern pattern = Pattern.compile("((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}");
        // 创建匹配给定输入与此模式的匹配器。
        Matcher matcher = pattern.matcher(str);
        //查找字符串中是否有符合的子字符串
        while (matcher.find()) {
            //查找到符合的即输出
//            System.out.println("查询到一个符合的手机号码：" + matcher.group());
            phone = matcher.group();
        }
        return phone;
    }


    /**
     * 解析地址
     *
     * @param address
     * @return
     * @author lin
     */
    public static List<Map<String, String>> addressResolution(String address) {
        String regex = "(?<province>[^省]+自治区|.*?省|.*?行政区|.*?市)(?<city>[^市]+自治州|.*?地区|.*?行政单位|.+盟|市辖区|.*?市|.*?县)(?<county>[^县]+县|.+区|.+市|.+旗|.+海域|.+岛)?(?<town>[^区]+区|.+镇)?(?<village>.*)";
        Matcher m = Pattern.compile(regex).matcher(address);
        String province = null, city = null, county = null, town = null, village = null;
        List<Map<String, String>> table = new ArrayList<Map<String, String>>();
        Map<String, String> row = null;
        while (m.find()) {
            row = new LinkedHashMap<String, String>();
            province = m.group("province");
            row.put("province", province == null ? "" : province.trim());
            city = m.group("city");
            row.put("city", city == null ? "" : city.trim());
            county = m.group("county");
            row.put("county", county == null ? "" : county.trim());
            town = m.group("town");
            row.put("town", town == null ? "" : town.trim());
            village = m.group("village");
            row.put("village", village == null ? "" : village.trim());
            table.add(row);
        }
        return table;
    }

}
