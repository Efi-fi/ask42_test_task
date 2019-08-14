var fields = 0;
$('#add_field').click(function() {
    $("#inputs").append(`<tr> <th> <input type="text" name="parameter_${fields}"> </th> <th> <input type="text" name="value_${fields}"> </th> </tr>`);
    fields += 1;
});
