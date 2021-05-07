;;; config.el -*- lexical-binding: t; -*-
;;
;; Copyright (C) 2021 John Doe
;;
;; Author: John Doe <http://github/billbrod>
;; Maintainer: John Doe <john@doe.com>
;; Created: May 07, 2021
;; Modified: May 07, 2021
;; Version: 0.0.1
;; Keywords:
;; Homepage: https://github.com/billbrod/config
;; Package-Requires: ((emacs 27.1) (cl-lib "0.5"))
;;
;; This file is not part of GNU Emacs.
;;
;;; Commentary:
;;
;;  
;;
;;; Code:

(require 'org)
(require 'ox)
(require 'ox-html)

;; Path for pygments or command name
(defvar pygments-path "pygmentize")

(defun pygments-org-html-code (code contents info)
  ;; Generating tmp file path.
  ;; Current date and time hash will ideally pass our needs.
  (setq temp-source-file (format "/tmp/pygmentize-%s.txt"(md5 (current-time-string))))
  ;; Writing block contents to the file.
  (with-temp-file temp-source-file (insert (org-element-property :value code)))
  ;; Exectuing the shell-command an reading an output
  (shell-command-to-string (format "%s -l \"%s\" -f html %s"
                   pygments-path
                   (or (org-element-property :language code)
                       "")
                   temp-source-file)))

(org-export-define-derived-backend 'pelican-html 'html
  :translate-alist '((src-block .  pygments-org-html-code)
                     (example-block . pygments-org-html-code)))

(provide 'config)
;;; config.el ends here
