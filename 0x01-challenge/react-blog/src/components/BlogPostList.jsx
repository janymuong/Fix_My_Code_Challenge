import React, { useState } from "react";
import { Link } from "react-router-dom";

const BlogPostList = ({ posts, page }) => {
  const [currentPagePosts, setCurrentPagePosts] = useState(posts);

  const handlePageChange = (event, newPage) => {
    setCurrentPagePosts(posts.slice((newPage - 1) * 10, newPage * 10));
  };

  return (
    <div>
      <ul>
        {currentPagePosts.map((post) => (
          <li key={post.id}>
            <Link to={`/blog/${post.id}`}>{post.title}</Link>
          </li>
        ))}
      </ul>
      <nav>
        <ul>
          {Array(Math.ceil(posts.length / 10)).map((i) => (
            <li key={i}>
              <Link
                onClick={() => handlePageChange(event, i + 1)}
                className={i === page - 1 ? "active" : ""}
              >
                {i + 1}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
};

export default BlogPostList;
