
import Post from "./Post";
import classes from "./PostList.module.css";

import { useLoaderData } from "react-router-dom";

function PostList() {

    const posts = useLoaderData();
    
    return (
        <>
            {posts.length > 0 && (
                <ul className={classes.postlist}>
                    {posts.map((post)=>(
                        <li>
                        <Post
                            key={post.title}
                            id={post.id}
                            PostTitle={post.title}
                            PostDesc={post.desc}
                            PostAuth={"~" + post.author}
                        />
                        </li>
                    ))}
                </ul>
            )}
           {posts.length === 0 && (
            <div>
                <h1>There is no post yet.</h1>
                <h4>Add your first post by clicking New Post</h4>
            </div>
           )}
        </>
    );
}

/* <Post PostTitle="Welcome" PostDesc="Welcome to the PostIt! This is thw first demo note in this React App." PostAuth="~Unknown"/> */

export default PostList;
