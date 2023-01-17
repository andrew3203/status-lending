function serializeForm(form_obj) {
  var form = form_obj.serializeArray();
  var res = {};
  form.forEach((element) => {
    res[element.name] = element.value;
  });
  return res;
}

$(function () {
  let submit_form_ids = "#f1, #f2, #f3, #f4";
  $(submit_form_ids).submit(function (event) {
    event.preventDefault();
    var form = $(this);

    var disabled = $(this).find(":input:disabled").removeAttr("disabled");

    var my_data = serializeForm($(this));
    my_data.site = parseInt(my_data.site);
    disabled.attr("disabled", "disabled");
    var action = $(this).attr("action");
    $.ajax({
      url: `https://${document.location.hostname}/api/${action}/`,
      type: "POST",
      data: my_data,
      success: function (data, textStatus, jqXHR) {
        form.hide();
        form.parent().find(".form-done").addClass( "visible" ).removeClass( "invisible" );
        form.parent().find(".form-fail").addClass( "invisible" ).removeClass( "visible" );
      },
      error: function (jqXHR, textStatus, errorThrown) {
        form.parent().find(".form-fail").addClass( "visible" ).removeClass( "invisible" );
      },
    });
    return false;
  });

  $(".close-icon-2").click(function (event) {
    $(".modal").css("display", "none");
  });

  $(".close-btn").click(function () {
    $(".modal").fadeOut(300);
    $(".modal").hide();
  });

  $(".open-modal").click(function () {
    $(".modal").fadeIn(300);
    $(".modal").show();
  });

  $(".open-modal2").click(function () {
    $(".modal2").fadeIn(300);
    $(".modal2").show();
  });

  $(".close-btn2").click(function () {
    $(".modal2").fadeOut(300);
    $(".modal2").hide();
  });
});
