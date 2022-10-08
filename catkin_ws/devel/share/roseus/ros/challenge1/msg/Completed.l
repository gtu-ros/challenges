;; Auto-generated. Do not edit!


(when (boundp 'challenge1::Completed)
  (if (not (find-package "CHALLENGE1"))
    (make-package "CHALLENGE1"))
  (shadow 'Completed (find-package "CHALLENGE1")))
(unless (find-package "CHALLENGE1::COMPLETED")
  (make-package "CHALLENGE1::COMPLETED"))

(in-package "ROS")
;;//! \htmlinclude Completed.msg.html


(defclass challenge1::Completed
  :super ros::object
  :slots (_completed ))

(defmethod challenge1::Completed
  (:init
   (&key
    ((:completed __completed) 0.0)
    )
   (send-super :init)
   (setq _completed (float __completed))
   self)
  (:completed
   (&optional __completed)
   (if __completed (setq _completed __completed)) _completed)
  (:serialization-length
   ()
   (+
    ;; float32 _completed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _completed
       (sys::poke _completed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _completed
     (setq _completed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get challenge1::Completed :md5sum-) "d06af43347051c04c834a8d2318f53e3")
(setf (get challenge1::Completed :datatype-) "challenge1/Completed")
(setf (get challenge1::Completed :definition-)
      "float32 completed

")



(provide :challenge1/Completed "d06af43347051c04c834a8d2318f53e3")


