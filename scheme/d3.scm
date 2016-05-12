;; scheme daily homework 3
;; name: Sam Rack
;; date: 01/21/15

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp15/scheme_dailies/d3/paradigms_d3.scm")
(use-modules (ice-9 paradigms_d3))

;; double
(define double 
  (lambda (n)
    (cond
      ((zero? n) 0)
      (else (add1 (add1 (double (sub1 n))))))))

;; tests!
(display (double 9))
(display "\n")

(display (double 2))
(display "\n")

(display (double 45))
(display "\n")

;; correct output:
;;   $ guile d3.scm
;;   18
;;   4
;;   90

