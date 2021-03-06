import React from 'react';
import PropTypes from 'prop-types';
import {Route, Switch} from 'react-router-dom';
import './styles.scss';
import Footer from 'components/Footer';
import Auth from 'components/Auth';

const App = props => [
  // Nav,
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,
  <Footer key={3} />,
];

App.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired,
};

// 로그인했을 때 보여지는 컴포넌트
const PrivateRoutes = props => (
  <Switch>
    <Route exact path="/" render={() => 'feed'} />
    <Route exact path="/explore" render={() => 'explore'} />
  </Switch>
);

//로그인을 하지 않았을때 보여지는 컴포넌트
const PublicRoutes = props => (
  <Switch>
    <Route exact path="/" component={Auth} />
    <Route exact path="/forgot" render={() => 'password'} />
  </Switch>
);

export default App;
