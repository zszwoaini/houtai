$(function () {
    $("select").change(function () {
        var $cur_btn = $(this);
        //拿到点击的那个订单的id
        var o_id = $(this).attr("o_id");
        console.log(o_id);
    //    要知道人家点了哪个option
        var op_value = $(this).find("option:selected").val();
        var op_text = $(this).find("option:selected").text();
        console.log(op_value);
    //    发请求
        $cur_btn.parents("tr").find(".o_status").html(op_text);
    })
})