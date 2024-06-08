import classes from "./Post.module.css";

import {Link} from 'react-router-dom';

function Post(props){
    
    return (
     <div>
        <Link to={props.id} className={classes.post}>
            <div>
                <h2>{props.PostTitle}</h2>
                <p>{props.PostDesc}</p>
            </div>
            <p className={classes.author}>{props.PostAuth}</p>
        </Link>
     </div>   
    );
}

export default Post;