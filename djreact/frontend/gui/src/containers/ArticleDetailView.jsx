import React, { Component } from "react";
import axios from "axios";

import { Card } from "antd";

class ArticleDetailView extends Component {
  state = {
    article: {}
  };

  componentDidMount() {
    const articleID = this.props.match.params.articleID;
    axios.get(`http://127.0.0.1:8000/api/${articleID}`).then(res => {
      this.setState({
        article: res.data
      });
    });
  }
  render() {
    return (
      <Card title={this.state.article.title}>{this.state.article.content}</Card>
    );
  }
}

export default ArticleDetailView;
