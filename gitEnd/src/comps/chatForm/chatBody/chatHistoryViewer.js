import React from 'react';
import useChatHistory from '../../../hooks/useChatContext';

const ChatHistoryViewer = () => {

  const { chatHistory } = useChatHistory();


  return (
    <div>
      <ul>
        {chatHistory.map((entry, index) => {
          console.log(entry, 'entry')
          return (
        <div key={index}>
          <label>User</label>
          <li>{entry.query}</li>
          <label>GitBot</label>
          <li>{entry.data}</li>
        </div>
          );
        }
        )}
      </ul>
    </div>
  );
};

export default ChatHistoryViewer;
