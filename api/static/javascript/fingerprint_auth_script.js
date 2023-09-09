//Login button configurations

const login_btn = document.getElementById('login_btn');

login_btn.addEventListener('mouseenter',() => {
    const login_btn_pic = document.getElementById('login_btn_pic');
    login_btn_pic.setAttribute('src','../images/login_btn_hover.png');
})

login_btn.addEventListener('mouseleave',() => {
    const login_btn_pic = document.getElementById('login_btn_pic');
    login_btn_pic.setAttribute('src','../images/login_btn.png');
})

