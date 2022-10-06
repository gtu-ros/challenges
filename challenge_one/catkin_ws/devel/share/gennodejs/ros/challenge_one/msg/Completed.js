// Auto-generated. Do not edit!

// (in-package challenge_one.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Completed {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.completed = null;
    }
    else {
      if (initObj.hasOwnProperty('completed')) {
        this.completed = initObj.completed
      }
      else {
        this.completed = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Completed
    // Serialize message field [completed]
    bufferOffset = _serializer.float32(obj.completed, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Completed
    let len;
    let data = new Completed(null);
    // Deserialize message field [completed]
    data.completed = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'challenge_one/Completed';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd06af43347051c04c834a8d2318f53e3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 completed
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Completed(null);
    if (msg.completed !== undefined) {
      resolved.completed = msg.completed;
    }
    else {
      resolved.completed = 0.0
    }

    return resolved;
    }
};

module.exports = Completed;
