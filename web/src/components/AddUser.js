import React, { Component } from "react";

import { connect } from "react-redux";

class AddUser extends Component {
  render() {
    return (
      <div>
        <h1>The form</h1>
        <label htmlFor="name">Firstname: </label>{" "}
        <input type="text" name="name" id="name" />
        <br />
        <label htmlFor="name">Surname: </label>{" "}
        <input type="text" name="surname" id="surname" />
        <br />
        <button>Register</button>
      </div>
    );
  }
}

export default connect()(AddUser);
