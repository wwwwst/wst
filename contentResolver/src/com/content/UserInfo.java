package com.content;

import java.util.List;


public class UserInfo {
    private String 姓名;
    private String 手机;
    private List<String> 地址;


    public String get姓名() {
        return 姓名;
    }

    public void set姓名(String 姓名) {
        this.姓名 = 姓名;
    }

    public String get手机() {
        return 手机;
    }

    public void set手机(String 手机) {
        this.手机 = 手机;
    }

    public List<String> get地址() {
        return 地址;
    }

    public void set地址(List<String> 地址) {
        this.地址 = 地址;
    }

    @Override
    public String toString() {
        return "UserInfo{" +
                "姓名='" + 姓名 + '\'' +
                ", 手机='" + 手机 + '\'' +
                ", 地址=" + 地址 +
                '}';
    }
}
