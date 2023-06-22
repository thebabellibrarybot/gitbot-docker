import React, { useState } from 'react';
import './textForm.css';
import useChatContext from '../../../hooks/useChatContext';
import { postMessage } from '../../../api/commonAPI';

const TextForm = () => {
  const [text, setText] = useState('');
  const { repo, updateChatHistory } = useChatContext();

  console.log(repo, 'repo')

  async function handleSend() {
    console.log(text);
    const msgObj = {
        qa_data: text,
        repo_url: repo.vector,
        repo_name: repo.data
    }
    console.log(msgObj, 'msgObj')
    const response = await postMessage(msgObj);
    if (response) {
        updateChatHistory(response);
    }
    setText('');
}

  function handleChange(e) {
    setText(e.target.value);
  }

  return (
    <div className="form-container">
      <textarea
        className="input-box"
        placeholder="Enter your questions here..."
        value={text}
        onChange={handleChange}
      />
      <button className="send-button" onClick={handleSend}>
        Send
      </button>
    </div>
  );
};
export default TextForm;