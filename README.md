# works
掌握技能：MongoDB+Python+NodeJS+AngularJS+RequiresJS+CSS3+SCSS+Gulp+MarkDown
功能简介：获取拉勾网上海站web前端招聘信息，自定义过滤条件，新增按公司地址，公司规模人数，简历处理及时率，简历处理用时等条件查询。PC/mobile页面，数据统计，显示图形，swiper&iscroll, 每24h更新一次数据库数据。分三个表：position,company,publisher;position关联company_id,publisher_id。职位加入“我的收藏”，用sessionStorage保存，发送收藏职位到邮箱然后清空收藏，页面卸载时也可以执行此操作。

## NodeJS篇

## MarkDown篇
MarkDown常用格式语法（[参考链接](http://www.cnblogs.com/hnrainll/p/3514637.html)）:
* 标题用#标示（1-6级）

  # 一级标题 （\# 一级标题）
  ## 二级标题 （\#\# 二级标题）
  ### 三级标题 （\#\#\# 三级标题）
* \*\-\+ 都可标示无序列表，数字标示有序列表，**标记后要加空格**
* 链接写法：\[链接文本\]\(链接地址\) "链接title内容"，*title部分可省略*
* 强调内容：\*\*粗体内容\*\*   \*斜体内容\*，**粗体**  *斜体*
* 转义符号用 \, 常用转移符如下

  + \\\\ 反斜杠
  + \\\` 反引号
  + \\\* 星号
  + \\\_ 下划线
  + \\\{\\\} 大括号
  + \\\[\\\] 中括号
  + \\\(\\\) 小括号
  + \\\# 井号
  + \\\+ 加号
  + \\\- 减号
  + \\\. 英文句号
  + \\\! 感叹号
* 引用 >
>  块注释（blockquote）
通过在文字开头添加“>”表示块注释。（当>和文字之间添加五个blank时，块注释的文字会有变化。）

* 代码引用

  单行代码用反单引号: \`\`
  `var s = 'ABC';`  
  代码块用缩进4个空格的段落:
  
      var str = "abc",
          arr = str.split[''];
      console.log(arr);

* 分隔线用\-\-\-， 下面是分隔线

---
