toggleSelect.addEventListener("change", () => {
  selectContent.classList.toggle("active");
});

function onChange(currentValue, prevValue, id) {
  const usage = document.getElementById(id);
  usage.value = currentValue - prevValue;
}

//한글적용을 위해 추가
$.datepicker.setDefaults({
  dateFormat: "yy-mm-dd",
  prevText: "이전 달",
  nextText: "다음 달",
  monthNames: [
    "1월",
    "2월",
    "3월",
    "4월",
    "5월",
    "6월",
    "7월",
    "8월",
    "9월",
    "10월",
    "11월",
    "12월",
  ],
  monthNamesShort: [
    "1월",
    "2월",
    "3월",
    "4월",
    "5월",
    "6월",
    "7월",
    "8월",
    "9월",
    "10월",
    "11월",
    "12월",
  ],
  dayNames: ["일", "월", "화", "수", "목", "금", "토"],
  dayNamesShort: ["일", "월", "화", "수", "목", "금", "토"],
  dayNamesMin: ["일", "월", "화", "수", "목", "금", "토"],
  showMonthAfterYear: true,
  yearSuffix: "년",
});
$(function () {
  $("#datepicker").datepicker();

  // $("#datepicker").datepicker("setDate", "today"); //(
});
$(function () {
  $(".time1").timepicker({
    timeFormat: "HH:mm",
    interval: 60,
    minTime: "1",
    maxTime: "23:00",
    defaultTime: "9",
    startTime: "01:00",
    dynamic: false,
    dropdown: true,
    scrollbar: true,
  });
});
$(function () {
  $(".time2").timepicker({
    timeFormat: "HH:mm",
    interval: 60,
    minTime: "1",
    maxTime: "23:00",
    defaultTime: "18",
    startTime: "01:00",
    dynamic: false,
    dropdown: true,
    scrollbar: true,
  });
});

function onCheck() {
  const requiredFirst = document.getElementById("required-input-1").value;
  const requiredSecond = document.getElementById("required-input-2").value;
  const requiredThird = document.getElementById("required-input-3").value;
  const requiredFourth = document.getElementById("required-input-4").value;
  if ((requiredFirst || requiredSecond) && requiredThird && requiredFourth) {
    alert("저장되었습니다!");
    return true;
  } else {
    alert("필수 입력사항을 입력해 주세요!");
    return false;
  }
}

