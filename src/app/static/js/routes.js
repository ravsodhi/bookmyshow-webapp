//page('/', authManager.requiresAuthentication);
page('/login', authManager.showLogin);
page('/logout', authManager.logout);
page('/register', authManager.showRegister);

page({});
//page.start();
