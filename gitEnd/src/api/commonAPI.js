import axios from "./axiosConfig";

async function postRepo (repoObj) {

    console.log(repoObj)

    try {
        const response = await axios.post('/repo/', repoObj);
        console.log(response)
        return response.data;
    } catch (error) {
        console.log(error)
    }
};
async function postMessage (msgObj) {

    console.log(msgObj, 'msgObj')

    try {
        const response = await axios.post('/chat/', msgObj);
        console.log(response)
        return response.data;
    } catch (error) {
        console.log(error)
    }
};
export { postRepo, postMessage };