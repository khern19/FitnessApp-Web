import React, { Component, Fragment } from 'react'
import ReactDOM from 'react-dom'

import { Provider } from 'react-redux'
import store from '../store'

import Header from './layout/Header'

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Fragment>
                    <Header />
                    <div></div>
                </Fragment>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'))
