function onCheck() {
  const requiredFirst = document.getElementById("required-input-1").value;
  const requiredSecond = document.getElementById("required-input-2").value;
  if (!!requiredFirst & !!requiredSecond) {
    alert("변경되었습니다!");
    return true;
  } else {
    alert("필수 사항을 입력해 주세요!");
    return false;
  }
}
