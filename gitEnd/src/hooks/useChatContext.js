import { useContext } from 'react';
import { ChatHistoryContext } from '../context/chatContext';

const useChatContext = () => {
  const { chatHistory, updateChatHistory, repo, updateRepo, repoList, updateRepoList } = useContext(ChatHistoryContext);

  return {
    chatHistory,
    updateChatHistory,
    repo,
    updateRepo,
    repoList,
    updateRepoList
  };
};

export default useChatContext;
