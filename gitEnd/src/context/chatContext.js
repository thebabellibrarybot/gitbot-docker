import React, { createContext, useState } from 'react';

// Create a new context
export const ChatHistoryContext = createContext();

// Create the provider component
export const ChatHistoryProvider = ({ children }) => {

  const [chatHistory, setChatHistory] = useState([]);
  const [repo, setRepo] = useState(null);
  const [repoList, setRepoList] = useState([]);

  // Function to update the chatHistory state by appending new chat object
  const updateChatHistory = (newChatObj) => {
    setChatHistory((prevChatHistory) => [...prevChatHistory, newChatObj]);
  };
  const updateRepoList = (newRepoObj) => {
    setRepoList((prevRepoList) => [...prevRepoList, newRepoObj]);
    };
  const updateRepo = async (repoObj) => {
    setChatHistory([]);
    setRepo(repoObj);
    const exists = repoList.some(repo => repo.name === repoObj.name && repo.url === repoObj.url);
    if (!exists) {
      updateRepoList(repoObj);
    }
  

  }


  // Value object to be provided by the context
  const contextValue = {
    chatHistory,
    updateChatHistory,
    repo,
    updateRepo,
    repoList,
    updateRepoList
  };

  return (
    <ChatHistoryContext.Provider value={contextValue}>
      {children}
    </ChatHistoryContext.Provider>
  );
};
