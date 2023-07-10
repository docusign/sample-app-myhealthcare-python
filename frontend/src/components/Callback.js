import React, { useEffect, useContext } from "react";
import { completeCallback } from "../api/auth";
import AppContext from "../context/appContext";
import { useNavigate } from "react-router-dom";

export const Callback = () => {
    let navigate = useNavigate();

    const { setLogged, setShowModal, setNextPage } = useContext(AppContext);

    useEffect(() => {
        completeCallback(setLogged, setShowModal);
        navigate(localStorage.getItem("nextPage"))
        setNextPage("");
    }, []);

    return (
        <>
        </>
    )
} 