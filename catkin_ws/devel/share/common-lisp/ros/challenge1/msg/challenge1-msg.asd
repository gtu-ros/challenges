
(cl:in-package :asdf)

(defsystem "challenge1-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Completed" :depends-on ("_package_Completed"))
    (:file "_package_Completed" :depends-on ("_package"))
  ))