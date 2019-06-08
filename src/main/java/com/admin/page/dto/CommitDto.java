package com.admin.page.dto;

public class CommitDto {
    private String nickName;
    private String gitId;
    private int commitCount;
    private String day;
    public String getNickName() {
        return nickName;
    }

    public void setNickName(String nickName) {
        this.nickName = nickName;
    }

    public String getGitId() {
        return gitId;
    }

    public void setValue(String gitId) {
        this.gitId = gitId;
    }

    public int getCommitCount() {
        return commitCount;
    }

    public void setCommitCount(int commitCount) {
        this.commitCount = commitCount;
    }
    public String getDay() {
        return day;
    }

    public void setDay(String day) {
        this.day = day;
    }
}
