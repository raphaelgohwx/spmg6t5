import axios from 'axios';

async function getStaffRoles() {
    try {
        const res = await axios.get("http://127.0.0.1:5001/getStaffRoles")
        return res
    }
    catch (err){
        console.log(err.message)
    }
}

export default {
    getStaffRoles: getStaffRoles
}

