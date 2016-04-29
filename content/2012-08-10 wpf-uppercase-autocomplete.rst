WPF Uppercase AutoComplete
##########################
:date: 2012-08-10 20:39
:author: bryan
:category: Blog
:slug: wpf-uppercase-autocomplete
:status: published

One of our clients wants uppercase characters in all of there inputs.
Unfortunately System.Windows.Controls.AutoCompleteBox doesn't support
the CharacterCasing option that is on a standard text box. My solution
is to simply inherit from AutoCompleteBox and after the template has
been applied grab the text box that is in the control and set it's
CharacterCasing to uppercase.

.. code-block:: c#

    public class UppercaseAutoComplete : AutoCompleteBox
    {
        public override void OnApplyTemplate()
        {
            base.OnApplyTemplate();
            TextBox actualTextBox = this.Template.FindName("Text", this) as TextBox;
            actualTextBox.CharacterCasing = CharacterCasing.Upper;
        }
    }
