;; scheme daily homework 5
;; name: Samnatha Rack
;; date: 01/19/15

;; sum*
(define sum*
  (lambda (ttup)
    (cond
      ((null? ttup) 0)
      ((list? (car ttup)) (+ (sum* (car ttup)) (sum* (cdr ttup))))  
      (else (+ (car ttup) (sum* (cdr ttup)))))))  

;; tests!
(display (sum* (list (list '5) (list))))
(display "\n")

(display (sum* (list (list '0) (list (list '0) (list (list '5) (list))) (list (list '0) (list (list '10) (list)))) ))
(display "\n")

(display (sum* (list (list '0) (list (list '0) (list (list '5) (list (list '7) (list)))) (list (list '0) (list (list '10) (list)))) ))
(display "\n")

(display (sum* (list (list '0) (list (list '0) (list (list '5) (list (list '7) (list)) (list (list '8) (list)))) (list (list '0) (list (list '10) (list)))) ))
(display "\n")

;; correct output:
;;   $ guile d5.scm
;;   5
;;   15
;;   22
;;   30

