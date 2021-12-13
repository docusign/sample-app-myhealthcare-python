import React from "react";

const BackdropLoader = props => {
    return (
        <div className={`backdrop ${props.backdrop && "backdrop-enable"}`}>

            {props.backdrop &&
                <div className="bubblingG">
                    <span id="bubblingG_1">
                    </span>
                    <span id="bubblingG_2">
                    </span>
                    <span id="bubblingG_3">
                    </span>
                </div>
            }
            
        </div>
    )
}
export default BackdropLoader;