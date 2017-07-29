<?php

namespace NethServer\Module\DelegatedPanel;

/**
 * Description of nethserver-delegation
 *
 * @author stephane de Labrusse <stephdl@de-labrusse.fr>
 */

class User extends \Nethgui\Controller\TableController
{

    public function initialize()
    {
        $columns = array(
            'Key',
            'sudo',
            'AdminAllPanels',
            'AdminPanels',
            'Actions'
        );

        $this
            ->setTableAdapter(new User\ListUsers($this->getPlatform()))
            ->setColumns($columns)
            ->addRowAction(new User\Modify('update'))
            ->addTableAction(new \Nethgui\Controller\Table\Help('Help'))

        ;
        parent::initialize();
    }


    public function prepareViewForColumnAdminAllPanels(\Nethgui\Controller\Table\Read $action, \Nethgui\View\ViewInterface $view, $key, $values, &$rowMetadata)
    {
        if ($values['AdminAllPanels'] == 'enabled' ) {
            return $view->translate('Enabled_label');
        }
        return $view->translate('Disabled_label');
    }

    public function prepareViewForColumnsudo(\Nethgui\Controller\Table\Read $action, \Nethgui\View\ViewInterface $view, $key, $values, &$rowMetadata)
    {
        if ($values['sudo'] == 'enabled' ) {
            return $view->translate('Enabled_label');
        }
        return $view->translate('Disabled_label');
    }

    public function prepareViewForColumnAdminPanels(\Nethgui\Controller\Table\Read $action, \Nethgui\View\ViewInterface $view, $key, $values, &$rowMetadata)
    {
        if ($values['AdminPanels'] !== '' and $values['AdminAllPanels'] == 'disabled') {
            return $view->translate('PanelDelegation');
        }
        return $view->translate('NoDelegation');
    }
}
