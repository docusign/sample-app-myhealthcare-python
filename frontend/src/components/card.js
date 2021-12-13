import React, { useContext } from "react";
import { Link } from "react-router-dom";
import AppContext from "../context/appContext";
import parse from "html-react-parser";

const Card = props => {
    const { setModalShow, logged, setNextPage } = useContext(AppContext);

    const onLogin = () => {
        setModalShow(true);
        setNextPage(props.linkTo);
    }

    return (
        <div className={`col h-card ${props.additionalClass}`}>
            <div className="h-card-body">
                <div className="h-card-top">
                    <img className="h-card-image" src={props.img} alt="" />
                    <h4 className="h-card-title">{props.title}</h4>
                    {logged &&
                    <Link to={props.linkTo} rel="noopener noreferrer">
                        <button className="h-card-button" type="button">
                            {props.getStarted}
                        </button>
                    </Link>
                    }
                    {!logged &&
                    <button className="h-card-button" type="button" onClick={onLogin}>
                        {props.getStarted}
                    </button>
                    }
                    <h5 className="h-card-features">
                        {props.featureTitle}
                    </h5>
                </div>
                <ul>
                    {parse(props.featureList)}
                </ul>
            </div>
        </div>
    )
}

export default Card;