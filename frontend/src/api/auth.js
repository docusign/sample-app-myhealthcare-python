import { handleError } from "./apiHelper";
import axios from './interceptors';

export async function codeGrantAuth() {
    try {
        await axios.get(
            process.env.REACT_APP_API_BASE_URL + "/code_grant_auth"
        );
    } catch (error){
        handleError(error);
    }
}

export async function completeCallback(setStatus, setShowModal) {
    try {
        await callback();
        await getStatus(setStatus);
    } catch (error){
        handleError(error, setShowModal)
    }
}

export async function callback() {
    try {
        const urlParams = new URLSearchParams(window.location.search);
        const code = urlParams.get('code');
        const response = await axios.post(
            process.env.REACT_APP_API_BASE_URL + "/callback",
            {
                code: code
            },
            {
                withCredentials: true
            }
        );
        return response.data.message
    } catch (error) {
        handleError(error);
    }
}

export async function logOut() {
    try {
        await axios.post(
            process.env.REACT_APP_API_BASE_URL + "/logout",
            {
                
            },
            {
                withCredentials: true
            }
        );
    } catch (error) {
        handleError(error);
    }
}

export async function getStatus(setStatus, history=undefined) {
    try {
        let response = await axios.get(
            process.env.REACT_APP_API_BASE_URL + "/get_status",
            {
                withCredentials: true
            }
        );
        setStatus(response.data.logged);
    } catch (error) {
        setStatus(false);
        history && history.push("");
        handleError(error);
    }
}

export async function jwtAuth() {
    try {
        await axios.post(
            process.env.REACT_APP_API_BASE_URL + "/jwt_auth",
            {
                
            },
            {
                withCredentials: true
            }
        );
    } catch (error){
        handleError(error);
    }
}
