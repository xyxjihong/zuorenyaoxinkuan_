import React, { useState } from 'react';
import PropTypes from 'prop-types';
import fetch from 'node-fetch';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const DummyInclude = (props) => {
    const {id, label, setProps, value} = props;
    const fetch_func = fetch;
    return (
        <div id={id}></div>
    );
}

DummyInclude.defaultProps = {};

DummyInclude.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string,

    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,

};

export default DummyInclude;
