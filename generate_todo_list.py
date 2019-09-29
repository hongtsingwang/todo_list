# coding=utf-8

import os
import sys
import datetime
import platform

system_str=platform.system()
print(system_str)

if system_str == "windows":
    todo_list_file = open("habit_file", encoding="utf-8")
    motto_file = open("motto", encoding="utf-8")
    longtime_file = open("longtime_job", encoding="utf-8")
    markdown_dir = os.path.join(os.getcwd(), "markdown")
    today = datetime.datetime.now().strftime("%Y%m%d")
    today_todo_list_file = open(os.path.join(markdown_dir, today + ".md"), "w", encoding="utf-8")
else:
    todo_list_file = open("habit_file")
    motto_file = open("motto")
    longtime_file = open("longtime_job")
    markdown_dir = os.path.join(os.getcwd(), "markdown")
    today = datetime.datetime.now().strftime("%Y%m%d")
    today_todo_list_file = open(os.path.join(markdown_dir, today + ".md"), "w")

week = datetime.datetime.now().strftime("%w")
if week == "0":
    week = "7"
info = ""


def write_habit():
    today_todo_list_file.write("# TODO LIST\n")
    today_todo_list_file.write("## 每日必做\n")
    index = 0
    for line in todo_list_file:
        try:
            line_list = line.strip().split()
            task_name, m, t, frequency = line_list
            frequency_list = frequency.split(",")
            if week in frequency_list:
                index += 1
                today_todo_list_file.write(str(index) + ". ")
                today_todo_list_file.write(task_name)
                today_todo_list_file.write(" -> %s" % t)
                today_todo_list_file.write("\n")
        except:
            print(line)
    today_todo_list_file.write("## 今日需做\n\n")
    today_todo_list_file.write("## 可做可不做\n\n")
    today_todo_list_file.write("\n")


def write_longtime():
    today_todo_list_file.write("## 长期任务\n")
    index = 0
    for line in longtime_file:
        try:
            line = line.strip()
            index += 1
            today_todo_list_file.write(str(index) + ". ")
            today_todo_list_file.write(line)
            today_todo_list_file.write("\n")
        except:
            print(line)
    today_todo_list_file.write("\n")


def write_motto():
    today_todo_list_file.write("# 格言\n")
    index = 0
    for line in motto_file:
        try:
            line = line.strip()
            index += 1
            today_todo_list_file.write(str(index) + ". ")
            today_todo_list_file.write(line)
            today_todo_list_file.write("\n")
        except:
            print(line)
    today_todo_list_file.write("\n")
    today_todo_list_file.write("# 每半个小时提醒自己\n")
    today_todo_list_file.write("\n" * 2)
    today_todo_list_file.write("# 努力目标\n")
    today_todo_list_file.write("## 截至昨日，目标还剩\n")

def write_jinzhan():
    today_todo_list_file.write("# 进展\n")
    today_todo_list_file.write("\n" * 2)


def write_summary():
    today_todo_list_file.write("# 总结\n")
    today_todo_list_file.write("\n" * 2)
    today_todo_list_file.write("## 值得记住的事情\n")
    today_todo_list_file.write("\n" * 2)
    today_todo_list_file.write("## 做的好的地方\n")
    today_todo_list_file.write("\n" * 2)
    today_todo_list_file.write("## 做的不好的地方\n")



if __name__ == "__main__":
    write_motto()
    write_habit()
    write_longtime()
    write_jinzhan()
    write_summary()
    today_todo_list_file.close()
