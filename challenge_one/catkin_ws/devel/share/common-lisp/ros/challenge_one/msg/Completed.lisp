; Auto-generated. Do not edit!


(cl:in-package challenge_one-msg)


;//! \htmlinclude Completed.msg.html

(cl:defclass <Completed> (roslisp-msg-protocol:ros-message)
  ((completed
    :reader completed
    :initarg :completed
    :type cl:float
    :initform 0.0))
)

(cl:defclass Completed (<Completed>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Completed>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Completed)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name challenge_one-msg:<Completed> is deprecated: use challenge_one-msg:Completed instead.")))

(cl:ensure-generic-function 'completed-val :lambda-list '(m))
(cl:defmethod completed-val ((m <Completed>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader challenge_one-msg:completed-val is deprecated.  Use challenge_one-msg:completed instead.")
  (completed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Completed>) ostream)
  "Serializes a message object of type '<Completed>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'completed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Completed>) istream)
  "Deserializes a message object of type '<Completed>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'completed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Completed>)))
  "Returns string type for a message object of type '<Completed>"
  "challenge_one/Completed")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Completed)))
  "Returns string type for a message object of type 'Completed"
  "challenge_one/Completed")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Completed>)))
  "Returns md5sum for a message object of type '<Completed>"
  "d06af43347051c04c834a8d2318f53e3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Completed)))
  "Returns md5sum for a message object of type 'Completed"
  "d06af43347051c04c834a8d2318f53e3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Completed>)))
  "Returns full string definition for message of type '<Completed>"
  (cl:format cl:nil "float32 completed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Completed)))
  "Returns full string definition for message of type 'Completed"
  (cl:format cl:nil "float32 completed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Completed>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Completed>))
  "Converts a ROS message object to a list"
  (cl:list 'Completed
    (cl:cons ':completed (completed msg))
))
