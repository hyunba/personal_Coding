const toggleBtn = document.querySelector('.navbar__toogleBtn');
// toggleBtn 이라는 변수에 document.querySelector를 이용해서 html 노드중에 클래스가 .navbar__toogleBtn 라는 아이를 할당해 준다.navbar
const menu = document.querySelector('.navbar__menu');
const icons = document.querySelector('.navbar__icons');

toggleBtn.addEventListener('click', () =>{
    menu.classList.toggle('active'); // 마우스 클릭시 menu와 icons의 클래스가 active가 없다면 active를 추가해주고 있다면 빼주는 일을함
    icons.classList.toggle('active');
}) // 이제 우리는 toggleBtn이 클릭 될 때마다 이벤트를 처리하는 일을 해야함