// Utilities
import { defineStore } from 'pinia'
import axios from "axios"

// Global variable
const serviceURL = import.meta.env.VITE_SERVICE_URL

export const useAppStore = defineStore('app', {
  state: () => ({
    loggedInUser: null,
    userID: null
}),
actions: {
  // async login (username) {
  //   try {
  //     const response = {username};
  //   if (response.status === 200) {
  //     this.saveResponsetoStore(response);
  //     this.saveUsertoLocalStorage();
  //   }
  //   return response;
  // }
  //   catch (error) {
  //     console.error(error);
  //     throw error;
  //   }
  // },
  saveResponsetoStore(role, userID) {
    this.loggedInUser = role;
    this.userID = userID;
    // this.saveUsertoLocalStorage();
  },
  // saveUsertoLocalStorage() {
  //   const item = window.localStorage.getItem("loggedInUser");
  //   console.log(this.loggedInUser);
  //   window.localStorage.removeItem("loggedInUser");
  //   window.localStorage.setItem("loggedInUser", JSON.stringify(this.loggedInUser)); 
  // },
  // loadUserFromLocalStorage() {
  //   const user = localStorage.getItem("loggedInUser");
  //   if (user) {
  //     this.loggedInUser = JSON.parse(user);
  //   }
  //   return user
  // },
  logout() {
    this.loggedInUser = null;
    this.userID = null;
  }
},
getters: {
  getCurrentUser() {
    return this.loggedInUser;
  },
  getCurrentUserID() {
    return this.userID;
  }
}
})


