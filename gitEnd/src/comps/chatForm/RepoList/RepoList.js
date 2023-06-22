import useChatContext from "../../../hooks/useChatContext";
import "./RepoList.css";
import { postRepo } from "../../../api/commonAPI";

const RepoList = () => {

    const { repoList, repo, updateRepo } = useChatContext();

    async function handleNewUrl (e) {
        if (e.length > 0) {
            const url = e;
            const parts = url.split('/'); 
            const lastPart = parts.pop();
            const part = lastPart.replace(/[^a-zA-Z0-9-_]/g, '');
            const repoObj = {
                repo_name: part,
                repo_url: url
            }
            const response = await postRepo(repoObj);
            if (response) {
                console.log('setting repoObj to state', response)
                updateRepo(response);
            }
        }
    };

    return (
        <div className="repolist">
            <h1>RepoList</h1>
            <input type="text" id="githubUrlInput" placeholder="Enter GitHub URL" onChange={(e) => handleNewUrl(e.target.value)}/>            
            {
                repoList.map((thisRepo, index) => {
                    console.log(thisRepo, 'thisRepo')
                    return (
                        <div key={index} className={thisRepo === repo ? "active" : "inactive"} onClick={()=>updateRepo(thisRepo)}>
                            <h1>{thisRepo.data}</h1>
                        </div>
                    )
                }
                )
            }
        </div>
    )
}
export default RepoList;