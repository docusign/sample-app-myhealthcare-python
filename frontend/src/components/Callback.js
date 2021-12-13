import React, { useEffect, useContext } from "react";
import { completeCallback } from "../api/auth";
import AppContext from "../context/appContext";
import { useHistory } from "react-router-dom";

export const Callback = () => {
    let history = useHistory();

    const { setLogged, setShowModal, setNextPage } = useContext(AppContext);

    useEffect(() => {
        completeCallback(setLogged, setShowModal);
        history.push(localStorage.getItem("nextPage"))
        setNextPage("");
    }, []);

    return (
        <>
        </>
    )
} 