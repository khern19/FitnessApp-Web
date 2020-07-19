import React, { Component, Fragment } from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Route, Switch, Redirect } from 'react-router-dom'

import { Provider } from 'react-redux'
import store from '../store'

import Header from './layout/Header'
import HomePage from './home/HomePage'

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router>
                    <Fragment>
                        <Header />
                        <div>
                            <Switch>
                                <Route exact path="/" component={HomePage} />
                            </Switch>
                        </div>
                    </Fragment>
                </Router>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))
