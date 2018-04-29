<%@ page contentType="text/html; charset=UTF-8" %>
<html>
<head>
<title>第一个JSP页面</title>
</head>
<body>
<h3>这是运行在Tomcat服务器下，创建的第一个JSP页面。</h3>
<h4>
<%
java.util.Date dt=new java.util.Date();
int year= dt.getYear();
year+=1900;
int month=dt.getMonth();
month+=1;
int date = dt.getDate();
int day = dt.getDay();
String str_year = String.valueOf(year);
String str_month = String.valueOf(month);
String str_date = String.valueOf(date);
String str_day = String.valueOf(day);
out.print("现在时间是"+str_year+"年");
out.print(str_month+"月");
out.print(str_date+"日");
out.print("星期"+str_day);
%>
</h4>

<script src="jquery-2.1.1.js">
</script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    alert("begin");
    $.post("http://localhost:8080/test/cgi-bin/oj_test/run1.py",
    {
      //name:"Donald Duck",
      //city:"Duckburg"
    },)
    // function(data,status){
    //   alert("数据：" + data + "\n状态：" + status);
    //}
    $.post("http://localhost:8080/test/cgi-bin/oj_test/run2.py",
    {
      //name:"Donald Duck",
      //city:"Duckburg"
    },
  );
  });
});
</script>
<button>向页面发送 HTTP POST 请求，并获得返回的结果</button>

<body>

</body>
</html>