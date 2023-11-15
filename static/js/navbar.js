class MobileNavbar {
  constructor(mobileMenu, navList, navLinks, notificationsIcon, notificationsList) {
    this.mobileMenu = document.querySelector(mobileMenu);
    this.navList = document.querySelector(navList);
    this.navLinks = document.querySelectorAll(navLinks);
    this.notificationsIcon = document.querySelector(notificationsIcon);
    this.notificationsList = document.querySelector(notificationsList);
    this.activeClass = "active";

    this.handleClick = this.handleClick.bind(this);
    this.handleNotificationsClick = this.handleNotificationsClick.bind(this);
  }

  animateLinks() {
    this.navLinks.forEach((link, index) => {
      link.style.animation
        ? (link.style.animation = "")
        : (link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`);
    });
  }

  handleClick() {
    console.log("Mobile menu clicked");
    this.navList.classList.toggle(this.activeClass);
    this.mobileMenu.classList.toggle(this.activeClass);
    this.animateLinks();
  }

  handleNotificationsClick() {
    console.log("Notifications icon clicked");
    this.notificationsList.classList.toggle(this.activeClass);
  }

  addClickEvent() {
    this.mobileMenu.addEventListener("click", this.handleClick);
    this.notificationsIcon.addEventListener("click", this.handleNotificationsClick);
  }

  init() {
    if (this.mobileMenu) {
      this.addClickEvent();
    }
    return this;
  }
}

const mobileNavbar = new MobileNavbar(
  ".mobile-menu",
  ".nav-list",
  ".nav-list li",
  ".notifications-icon-nav",
  ".notifications-list-nav"
);
mobileNavbar.init();
