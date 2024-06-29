import React from 'react'
import Cookies from 'universal-cookie'


const cookies = new Cookies();

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      error: "",
      isauthenticated: false,
    };
  }

  componentDidMount = () => {
    this.getSession();
  }

  getSession = () => {
    fetch("/accounts/session/", {
      credential: "same-origin",
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.isauthenticated) {
        this.getState({isauthenticated: true});
      }
      else {
        this.setState({isauthenticated: false});
      }
    })
    .catch((err) => {
      console.log(err);
    });
  }

  whoami = () => {
    fetch("/accounts/whoami/", {
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "same-origin",
    })
    .then((res) => res.json())
    .then((data) => {
      console.log("You're logged in as: " + data.username);
    })
    .catch((err) => {
      console.log(err);
    });
  }

  handlePasswordChange = (event) => {
    this.setState({password: event.target.value});
  }

  handleUsernameChange = (event) => {
    this.setState({username: event.target.value});
  }

  isResponseOk(response) {
    if (response.status >= 200 && response.status <= 299) {
      return response.json();
    }
    else {
      throw Error(response.statusText);
    }
  }

  login = (event) => {
    console.log(this.state.username)
    event.preventDefault();
    fetch("accounts/login/", {
      method: "POST",
      headers : {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies.get("csrftoken"), 
      },
      credentials: "same-origin",
      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password
      }),
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({
        isauthenticated: true,
        username: "",
        password: "",
        error: ""
      })
    })
    .catch((err) => {
      console.log(err);this.setState({
        error: "Wrong username or password"
      })
    });
  }

  logout = () => {
    fetch("accounts/logout", {
      credentials: "same-origin",
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({
        isauthenticated: false
      });
    })
    .catch((err) => {
      console.log(err);
    })
  }

  render() {
    if (!this.state.isauthenticated) {
      return (
        <div className="container mt-3">
          <h1> React Cookie Auth </h1>
          <br></br>
          <form onSubmit={this.login}>
            <div className="form-group">
              <label htmlFor="username"> Username </label>
              <input type="text" className='form-control' 
              name="login_username" id="username"
              value={this.state.username}
              onChange={this.handleUsernameChange}></input>
            </div>  
            <div className="form-group">
              <label htmlFor="password"> Password </label>
              <input type="password" className='form-control' 
              name="login_password" id="password" 
              value={this.state.password} 
              onChange={this.handlePasswordChange}></input>
              <div>
                {this.state.error && <small className='text-danger'> {this.state.error} </small>}
              </div>
            </div>
            <button type="submit" className="btn btn-primary"> Login </button>
          </form>
        </div>
      );
    }
    return (
      <div className="container-mt-3">
        <h1> React Cookie Auth </h1>
        <p> You are logged in </p>
        
        <button className="btn btn-primary-mr-2"> WhoAmI? </button>
        <button className="btn btn-danger"> Logout </button>
      </div>
    )
  }
};

export default App;