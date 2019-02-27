$(function () {
    $(".delete_btn").click(function () {
    //    获取点击的那个按钮所对应的商品id
        var g_id = $(this).attr("i_id");
        var $current_btn = $(this);
        $.ajax({
            url:"/api/item",
            method:"delete",
            data:{
                "g_id": g_id
            },
            success: function (res) {
            //    如果删除成功了， 那么就需要删除
                if (res.code == 1){
                    //删除整个tr
                    $current_btn.parents("tr").remove();
                } else {
                    alert(res.msg);
                }
            }
        })
    })
})