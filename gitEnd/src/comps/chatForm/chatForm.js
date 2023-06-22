import './chatform.css'
import ChatHistoryViewer from './chatBody/chatHistoryViewer';
import useChatContext from '../../hooks/useChatContext';
import SideBar from './RepoList/RepoList';
import { useRef, useEffect } from 'react';
import TextForm from './chatMouth/textForm';


const ChatForm = ({ onToggle, chatOpen }) => {

    const { repo, chatHistory } = useChatContext();
    const chatHistoryRef = useRef(null);

    useEffect(() => {
        if (chatHistoryRef.current) {
            // Scroll to the bottom of the container
            chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
          }
    }, [chatHistory]);


    return (
        <div className="full-flex split-flex">
            
            <img src={process.env.PUBLIC_URL + `/icon.svg`} alt="profile pic" className='sm-icon' onClick={onToggle}/>

            <div className="sidebar basic-border basic-box">

                <SideBar />
                
            </div>

            <div className="flex-body">

                <div className="chat-head basic-border basic-box">
                    <h1>{repo? repo.data:null}</h1>
                </div>

                <div className="chat-body basic-border basic-box" ref = {chatHistoryRef}>
                    <ChatHistoryViewer />
                </div>

                <div className="chat-bar basic-border basic-box">
                    <TextForm />
                </div>

            </div>
        </div>
    )
}
export default ChatForm;