// head will manage wether the chat is open or not. it will also contain all the context inside of it
import { useState } from 'react';
import ChatForm from "../chatForm/chatForm";
import { ChatHistoryProvider } from '../../context/chatContext';


const Head = () => {

    const [chatOpen, setChatOpen] = useState(false);

    function handleToggle() {
        setChatOpen(!chatOpen);
    }

    return (

        <div className="head">

            <ChatHistoryProvider>

            {
                chatOpen ? 
                <div className="big-icon svg-button icon-position"> 
                    <ChatForm onToggle={ handleToggle } chatOpen={ chatOpen }/>
                </div>
                :
                <div className="chat closed" onClick={handleToggle}>
                    <img src={process.env.PUBLIC_URL + `/icon.svg`} alt="profile pic" />
                </div>
            }

            </ChatHistoryProvider>
        
        </div>
    )

}
export default Head;