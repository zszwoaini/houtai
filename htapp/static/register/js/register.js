$(function(){
    $("#btn").click(function () {
        //先获取用户输入的数据
        var email = $("#email").val();
        var pwd = $("#pwd").val();
        var confirm_pwd = $("#pwd_confirm").val();
        //判断用户数据格式
        if (email.length<=3){
            alert("邮箱不正确")
        }
        if (pwd.length < 3){
            alert("太短了")
        }
        if (confirm_pwd != pwd){
            alert("两次输入密码不匹配")
        }
        $.ajax({
            url:'/api/register',
            method:'post',
            data:{
                email:email,
                pwd:md5(pwd),
                confirm_pwd:md5(confirm_pwd)
            },
            success:function(res){
                if (res.code == 1){
                    window.open(res.data,target='_self')

                }else {
                    alert(res.msg)
                }
        }
        })
    })
})