// Utilities
import { defineStore } from 'pinia'
import axios from "axios"

// Global variable
const serviceURL = import.meta.env.VITE_SERVICE_URL

export const useAppStore = defineStore('app', {
  state: () => ({
  apiURL: serviceURL
  }),
  actions: {
    async getStaffRoles() {

      apiURL = `${serviceURL}/getStaffRoles`

      try {
        const response = await axios.get(apiURL);

        if (response.status === 200) {
          return response
        }

      } catch (error) {
        console.error("error when getting staff roles")
      }
      // if (response.ok){
      //   // console.log(result)

      //   let html = "";
      //   for (let i = 0; i<result.length; i++){
      //     html+= 
      //     `<div style="background-color: rgb(255, 245, 224); height: 100px; width: 500px; margin-top: 10px;">`

      //     html+= "<h2>" + result[i].Role_Name + "</h2>"
      //     html+= "<h5>" + result[i].Role_Description + "</h5>"
      //     html+= "<h6> Role Deadline: " + result[i].Date_Closed + "</h6>"

      //     html+= `</div>`
      //   }
      //   document.getElementById("roleListings").innerHTML=html;
      // }
    }



  }


})


