import axios from 'axios';

async function getAllRoleListings() {
    try {
        const res = await axios.get("http://127.0.0.1:5001/getAllRoleListings")
        return res
    }
    catch (err){
        console.log(err.message)
    }
}

async function getActiveRoleListings() {
    try {
        const res = await axios.get("http://127.0.0.1:5001/getActiveRoleListings")
        return res
    }
    catch (err){
        console.log(err.message)
    }
}

async function getAllStaffName() {
    try {
        const res = await axios.get("http://127.0.0.1:5001/getAllStaffName")
        return res
    }
    catch (err){
        console.log(err.message)
    }
}

export default {
    getAllRoleListings: getAllRoleListings,
    getActiveRoleListings: getActiveRoleListings,
    getAllStaffName, getAllStaffName
}

