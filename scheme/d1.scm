;; Samantha Rack
;; Programming Paradigms
;; Scheme Daily 1

;; this is how to load external modules in scheme
;(load-from-path "/home/cmc/teaching/cse332_sp15/svn/assignments/scheme_dailies/d1/public/paradigms_d1.scm")
(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp15/scheme_dailies/d1/paradigms_d1.scm")
(use-modules (ice-9 paradigms_d1))

;; the list q
;; notice it has a ' in front of the list; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define q '(turkey (gravy) (stuffing potatoes ham) peas))

;; question 1
(display "question 1: ")
(display (atom? (car (cdr (cdr q)))))
(display "\n")
;; output: 
;;	#f
;;
;; explanation:
;; (use as many lines as necessary, just add more comments)
;; 	The innermost cdr q outputs ((gravy) (stuffing potatoes ham) peas), 
;; 	the next cdr outputs ((stuffing potatoes ham) peas), and the 
;; 	car outputs (stuffing potatoes ham).  atom? returns true (#t) if the
;;	argument is unorganized data, but since (stuffing potatoes ham) is a list,
;;	atom? returns #f (false)

;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;;	#t
;;
;; explanation:
;;	This question performs the same operations on q, eventually returning 
;;	(stuffing potatoes ham) to be operated on by lat?. lat? returns true when
;;	its argument is a list of atoms. (stuffing potatoes ham) is a list of atoms,
;;	so the output is #t


;; question 3
(display "question 3: ")
(display (cond ((atom? (car q)) (car q)) (else '())))
(display "\n")
;; output:
;;	turkey
;;
;; explanation:
;;	car q returns turkey, which is an atom.  So the first element in the list
;; 	argument provided to cond is #t. The cond function then outputs car q, since
;;	the first element in the list gave #t and car q is the second element in the
;;	list. Had atom? (car q) been false, then the third item in the list, (else'()),
;;	would have executed.  Because car q is turkey, that is the output.
